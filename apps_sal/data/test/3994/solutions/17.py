n = int(input())
on_time = [0] * 50010

s = input()
for i in range(n):
    a, b = list(map(int, input().split()))
    sec = 0
    if s[i] == "1":
        for j in range(b):
            on_time[j] += 1
        sec = b+a
        while sec <= 50000:
            for j in range(sec, sec+a):
                on_time[j] += 1
            sec += 2*a
    else:
        sec = b
        while sec <= 50000:
            for j in range(sec, sec+a):
                on_time[j] += 1
            sec += 2*a

print(max(on_time))

