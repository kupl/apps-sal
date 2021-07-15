N = int(input())
ans = [] if N != 0 else [0]
while N:
    ans.append(-(N % -2))
    N = -(N // 2)
print(("".join(map(str, ans[::-1]))))

