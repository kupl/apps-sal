n=int(input())
sizes=sorted(list(set(map(int, input().split(' ')))))

def isThree(z):
    for i in range(2,len(z)):
        if abs(z[i-2]-z[i])<=2:
            return True
    return False

if isThree(sizes):
    print("YES")
else:
    print("NO")
