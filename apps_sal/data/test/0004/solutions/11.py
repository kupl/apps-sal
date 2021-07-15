x = int(input())
hh, mm = map(int, input().split())
mins = hh * 60 + mm
ans = 0
while str(mins // 60).count('7') == 0 and str(mins % 60).count('7') == 0:
    mins -= x
    ans += 1
    if mins < 0:
        mins = 1440 + mins
print(ans)
