# -*- coding:utf-8 -*-

in_gate = []
out_gate = []
N, M = map(int, input().split())
for _ in range(M):
    temp_l, temp_r = map(int, input().split())
    in_gate.append(temp_l)
    out_gate.append(temp_r)

ans_bef = min(out_gate) - max(in_gate)
if ans_bef < 0:
    print(0)
else:
    print(ans_bef + 1)
