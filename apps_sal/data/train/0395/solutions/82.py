class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        increasing = [(v, i) for (i, v) in enumerate(A)]
        increasing.sort()
        increasing = [item[1] for item in increasing]
        decreasing = [(v, i) for (i, v) in enumerate(A)]
        decreasing.sort(key=lambda item: item[0] * -1)
        decreasing = [item[1] for item in decreasing]
        odds_next = make(increasing)
        evens_next = make(decreasing)
        odds = [False for i in range(len(A))]
        odds[len(A) - 1] = True
        evens = [False for i in range(len(A))]
        evens[len(A) - 1] = True
        results = [len(A) - 1]
        for i in reversed(list(range(len(A) - 1))):
            if odds_next[i] > i and evens[odds_next[i]]:
                odds[i] = True
                results.append(i)
            if evens_next[i] > i and odds[evens_next[i]]:
                evens[i] = True
        print(results)
        return len(results)


def make(arr):
    output = [i for i in range(len(arr))]
    stack = []
    for i in range(len(arr)):
        value = arr[i]
        while stack and value > stack[-1]:
            index = stack.pop()
            output[index] = value
        stack.append(value)
    return output
