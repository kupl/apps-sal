# とある世界では、今日はクリスマスイブの前日です。高羽氏は、デパートでN個の品物を買おうとしています。i個目の品物(1≤i≤N)の定価はpi円です。
# 彼は割引券を持っており、N個のうち最も定価が高い品物1個を定価の半額で買うことができます。残りのN−1個の品物に対しては定価を支払います。
# 支払金額は合計でいくらになるでしょうか？

N = int(input())
list = [int(input()) for i in range(N)]

expensive = max(list)
discount = expensive // 2
total = sum(list) - expensive + discount

print(total)
