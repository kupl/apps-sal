s = input()

answer = 0
last = s.find("bear") + 1
answer += last * (len(s) - last - 2)
s = s[: last - 1] + "
last += 1
while "bear" in s:
    i = s.find("bear") + 1
    answer += (i - last + 1) * (len(s) - i - 2)
    s = s[: i - 1] + "
    last = i + 1

print(answer)
