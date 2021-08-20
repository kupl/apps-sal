N = int(input())
(*A,) = map(int, input().split())
b = 0
i = 1
for a in A:
    if a == i:
        i += 1
    else:
        b += 1
print(b if b != N else -1)
