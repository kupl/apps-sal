i = int(input())
ir = i % 10
iq = i // 10
if(i == 12):
    print("YES")
elif(ir == 1 or ir == 7 or ir == 9):
    print("NO")
elif(iq == 1 or iq == 7 or iq == 9 or iq == 2):
    print("NO")
else:
    print("YES")
