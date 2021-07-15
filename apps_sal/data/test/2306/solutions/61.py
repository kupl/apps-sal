#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def mileage(t, v, vl, vr):
    assert(0 <= vl <= v and 0 <= vr <= v)
    # 最高速度v, 左端での速度vl, 右端での速度vr, 秒数tの時の走行距離を求める
    l = v-vl
    r = t-(v-vr)
    if l > r:
        tmp = (l+r)/2
        l = tmp
        r = tmp
    ret = 0
    ret += l*l/2+vl*l
    ret += (r-l)*v
    ret += (t-r)*vr+(t-r)*(t-r)/2
    return ret

def main():
    n = ri()
    lt = rli()
    lv = rli()
    lt.append(0)
    lv.append(0)
    lefts = [0] # 各区間の左端での列車の速度
    for i in range(n):
        left = min(lefts[i]+lt[i], lv[i], lv[i+1])
        offset = 0
        for j in range(i+1, n+1):
            left = min(left, offset+lv[j])
            offset += lt[j]
        lefts.append(left)
    # print(lefts)
    ans = 0
    for i in range(n):
        ans += mileage(lt[i], lv[i], lefts[i], lefts[i+1])
    print(ans)


def __starting_point():
    main()

__starting_point()
