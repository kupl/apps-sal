import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    s = input().rstrip()
    changes = 1
    spare = 0
    before = s[0]
    spare_can = 1
    for j in range(n-1):
        if s[j+1] == before:
            if spare_can > 0:
                spare_can -= 1
                spare += 1
        else:
            before = s[j+1]
            changes +=1
            spare_can +=1
    ans = 0
    ans += spare
    changes-=spare
    ans += (changes+1)//2
    print(ans)   
