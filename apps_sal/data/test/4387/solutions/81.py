r = int(input())
if r < 1200:
    ans = 'ABC'
elif 1200 <= r < 2800:
    ans = 'ARC'
else:
    ans = 'AGC'
print(ans)
