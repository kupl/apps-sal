N = input()
answer = list(N)

if answer[0] == answer[1] == answer[2]:
    print("Yes")
elif answer[1] == answer[2] == answer[3]:
    print("Yes")
else:
    print("No")
