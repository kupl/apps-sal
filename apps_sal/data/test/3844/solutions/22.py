n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
num = [a[0]]
cnt = [1]
for i in range(1, len(a)):
    if a[i] == num[-1]:
        cnt[-1] += 1
        continue
    num.append(a[i])
    cnt.append(1)
ans = "Agasa"
for i in cnt:
    if i%2 == 1:
        ans = "Conan"
print(ans)

