import sys


def input():
    return sys.stdin.readline().rstrip()


def input_split():
    return [int(i) for i in input().split()]


testCases = int(input())
answers = []
for _ in range(testCases):
    # take input
    n = int(input())
    arr = input_split()

    counts = {a: 0 for a in arr}
    for a in arr:
        counts[a] += 1

    temp = list(counts.values())
    temp.sort()
    temp.reverse()

    k = 0
    val = temp[0]
    ptr = 1
    while(ptr < len(temp)):
        if temp[ptr] != val:
            break
        ptr += 1
        k += 1

    n = n - k

    # if val == 1:
    # val cant be 1
    ans = (n - val) // (val - 1)

    answers.append(ans)

print(*answers, sep='\n')
