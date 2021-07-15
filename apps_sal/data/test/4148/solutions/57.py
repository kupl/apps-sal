a = [chr(i) for i in range(65, 65+26)]
n = int(input())
s = input()
ans = ''
for i in s:
    ans += (a[(a.index(i)+n)%26])
print(ans)
