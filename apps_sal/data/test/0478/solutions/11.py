n = int(input())
s = list(input())
k = 0
answer = 0
while k == 0:
    k = 1
    mas = []
    for i in range(1, len(s)):
        if ord(s[i]) - 1 == ord(s[i - 1]):
            k = 0
            mas.append([ord(s[i]), i])
        elif ord(s[i]) + 1 == ord(s[i - 1]):
            k = 0
            mas.append([ord(s[i - 1]), i - 1])
    if mas:
        mas.sort()
        answer += 1
        ind = mas[-1][1]
        s.pop(ind)
print(answer)
