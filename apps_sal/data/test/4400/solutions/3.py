S = input()
ans = 0
if S == "SSS":
    ans = 0
elif S == "SSR":
    ans = 1
elif S == "SRS":
    ans = 1
elif S == "RSS":
    ans = 1
elif S == "SRR":
    ans = 2
elif S == "RSR":
    ans = 1
elif S == "RRS":
    ans = 2
else:
    ans = 3

print(ans)
