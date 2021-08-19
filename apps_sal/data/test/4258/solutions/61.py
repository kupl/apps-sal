def input2():
    return map(int, input().split())


(a, b, t) = input2()
ans = 0
for i in range(1, 21):
    if a * i > t:
        break
    ans += b
print(ans)
