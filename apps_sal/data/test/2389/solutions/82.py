# greedyな選択：数字が小さいほうを増やし大きいほうを減らす。等しい場合どっちでもいい（とりあえず左を増やす）。
# 
# 初手 1 1 1 なら絶対成功 (greedy)
# どこかの状態で 1 1 1 を作れるなら絶対成功 (greedy)
# 0 1 2 なら絶対成功 (greedy)
# 0 0 3 で、初手がAB以外なら絶対成功 (greedy)
# 0 0 0 なら絶対失敗
#
# 初手で成否が分からないのは
# 0 1 1
# 0 0 2
# 0 0 1
#
# 0 0 1 は greedyにやるしかない
# 0 0 2 は、少なくとも1回はgreedy
#
# 結局、各回のgreedyでは問題になるのは
# 0 1 1 で 1 1 のペアでどっちを増やすか選ぶときのみ
# これは1個先を読めば十分


def select(x, y, ops, i, z):
    # true -> x を増やす
    if not(x == 1 and y == 1 and z == 0 and i < len(ops) - 1):
        if x <= y:
            return True
        else:
            return False

    # x = y = 1, z = 0, i < len(ops) - 1
    # 先読みして xz なら x を増やす
    # 先読みして xy なら y を増やす
    # 先読みして xy なら どっちでもいい
    op = ops[i]
    nop = ops[i+1]

    oo = (op, nop)
    if oo in [("AB", "AC"), ("BC", "AB"), ("AC", "AB")]:
        return True

    return False

def main():
    nabc = [int(_x) for _x in input().split()]
    n = nabc[0]
    a = nabc[1]
    b = nabc[2]
    c = nabc[3]

    ops = []
    for i in range(n):
        ops.append(input())

    result = []
    for i in range(n):
        op = ops[i]
        if op == "AB":
            if select(a, b, ops, i, c):
                result.append("A")
                a+=1
                b-=1
            else:
                result.append("B")
                a-=1
                b+=1
        if op == "AC":
            if select(a, c, ops, i, b):
                result.append("A")
                a+=1
                c-=1
            else:
                result.append("C")
                a-=1
                c+=1
        if op == "BC":
            if select(b, c, ops, i, a):
                result.append("B")
                b+=1
                c-=1
            else:
                result.append("C")
                b-=1
                c+=1
        if a <0 or b<0 or c<0:
            print("No")
            return

    print("Yes")
    for r in result:
        print(r)

main()

