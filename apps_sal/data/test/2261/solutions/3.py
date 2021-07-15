import sys

def check(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            diff = 0
            for k in range(n):
                if arr[i][k] == arr[j][k]:
                    diff += 1
                else:
                    diff -= 1
            if diff:
                return (arr[i], arr[j])
    return False

def inv(arr):
    return [(not x) for x in arr]

def gen(n):
    if n == 1:
        return [[True]]
    curr = gen(n // 2)
    ans = []
    ans.extend((x +     x  for x in curr))
    ans.extend((x + inv(x) for x in curr))
    return ans

k = int(input())
ans = gen(2 ** k)
for x in ans:
    sys.stdout.write("".join(["+" if el else "*" for el in x]))
    sys.stdout.write("\n")
