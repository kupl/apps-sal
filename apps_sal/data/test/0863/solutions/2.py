a, t1 = map(int, input().split())
b, t2 = map(int, input().split())
hour, minute = map(int, input().split(':'))
minutef = minute + hour * 60 + t1
minutes = minute + hour * 60 - t2
cnt = 0
time = 300

while time < minutef and time < 240 * 6:
    if time > minutes:
        cnt += 1
    time += b
print(cnt)
