import fractions
import sys

N, X, D = list(map(int, input().split()))

"""

X+0D
X+1D
X+2D
...
X+(N-1)D

からとってくる

aX + bD

aX中にlcmがtこあるとき、 newa = (aX-t*lcm) // X = a - t*lcm//X
newl += lcm*t // D

で、aX > lcm(X,D)だったらaをへらして?の範囲をうしろにずらす
各aについて計算量はO(1)

3,4,2のとき
4
6
8
lcm = 4

0,4,6,8,10,12,14,18

XD両方負だと問題なし
Dが負の時 >> 大事なのは aXを変換できるならDにする>aを減らす
?X > !Dにする

X  D
3 -3

X + 0D = 3
X + 1D = 0

0X = 0
1X + 

lcm = 3
なので,0は X+-1Dに変換可能

0 100 200 300

"""

if X == 0 and D == 0:
    print((1))
    return
elif D == 0:
    print((N + 1))
    return
elif X == 0:
    print((N * (N - 1) // 2 + 1))
    return

l = [[] for i in range(N + 1)]
r = [[] for i in range(N + 1)]
lcm = X * D // fractions.gcd(X, D)


bl = 0
br = 0


for a in range(N + 1):

    if a > 0:
        bl += a - 1
        br += N - a

    #print (bl,br)

    t = (a * X) // lcm
    #print (a,t*lcm//X)
    a -= t * lcm // X

    l[a] .append(bl + lcm * t // D)
    r[a] .append(br + lcm * t // D)

ans = 0


for a in range(N + 1):

    now = 0
    nl = 0
    lind = 0
    rind = 0
    l[a].sort()
    r[a].sort()

    for i in range(2 * len(l[a])):

        if rind == len(r[a]) or (lind != len(l[a]) and l[a][lind] <= r[a][rind]):
            if now == 0:
                nl = l[a][lind]
            now += 1
            lind += 1
        else:
            now -= 1
            if now == 0:
                ans += r[a][rind] - nl + 1
            rind += 1


#print (l)
#print (r)
print(ans)
