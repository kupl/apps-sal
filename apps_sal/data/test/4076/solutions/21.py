import math
def i_input(): return int(input())


def i_map(): return list(map(int, input().split()))


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]
def degCal(hour,minite):
    ansDeg=0
    convHour=hour+minite/60
    angA=2*math.pi/12*convHour
    angB=2*math.pi*convHour
    ansDeg=abs(angA-angB)

    return ansDeg

def lenCal(deg,lenA,lenB):
    ansLen=math.sqrt(lenA**2+lenB**2-2*lenA*lenB*math.cos(deg))

    return ansLen

a,b,h,m= i_map()
angle=degCal(h,m)
ans=lenCal(angle,a,b)

print(ans)




