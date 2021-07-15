S = input()
ans = 0
if 'RRR' in S:
    ans += 3
elif 'RR' in S:
    ans += 2
elif 'R' in S:
    ans += 1
print(ans)
