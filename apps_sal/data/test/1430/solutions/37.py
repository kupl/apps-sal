(n, k) = list(map(int, input().split()))
s = input()
sento = 0
ketu = 0
tmp = '1'
zeroichi = []
cnt = 0
for i in range(n):
    if tmp == s[i]:
        cnt += 1
    else:
        zeroichi.append(cnt)
        cnt = 1
        tmp = s[i]
zeroichi.append(cnt)
if len(zeroichi) % 2 == 0:
    zeroichi.append(0)
if len(zeroichi) == 1:
    zeroichi.append(0)
    zeroichi.append(0)
i = 0
ans = 0
ans_list = []
j = 0
right = min(1 + k * 2, len(zeroichi))
left = 0
while i != right:
    ans += zeroichi[i]
    i += 1
ans_list.append(ans)
while right != len(zeroichi):
    ans -= zeroichi[left]
    ans -= zeroichi[left + 1]
    ans += zeroichi[right]
    ans += zeroichi[right + 1]
    ans_list.append(ans)
    left += 2
    right += 2
print(max(ans_list))
