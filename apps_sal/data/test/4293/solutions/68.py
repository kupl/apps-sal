P, Q, R = map(int, input().split())

ans = [P+Q, Q+R, R+P]
print(min(ans))
