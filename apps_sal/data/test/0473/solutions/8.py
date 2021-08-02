s = input().strip()
p = input().strip()
ans = int(s[:2]) * 60 + int(s[3:]) - int(p[:2]) * 60 - int(p[3:])
ans = ans % 1440
t = ('0' if ans // 60 < 10 else '') + str(ans // 60) + ':' + ('0' if ans % 60 < 10 else '') + str(ans % 60)
print(t)
