n = int(input())
card_ls = list(map(int, input().split()))
card_ls.sort()
have_to_eat = 0
for i in range(1, n):
    if card_ls[i - 1] == card_ls[i]:
        have_to_eat += 1
if have_to_eat % 2 == 1:
    have_to_eat += 1
ans = n - have_to_eat
print(ans)
