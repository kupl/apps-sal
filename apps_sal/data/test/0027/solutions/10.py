n = int(input())
s = input()
currents = s
ans = 0
while len(currents) > 0:
    if len(currents) % 2 == 0 and currents[0:len(currents) // 2] == currents[len(currents) // 2:len(s)]:
        ans = ans + len(currents) // 2
        ans += 1
        break
    else:
        currents = currents[0:len(currents) - 1]
        ans = ans + 1
print(ans)
