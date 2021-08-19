A, B, N = map(int, input().split())
# たしかに周期性があるため、この例でいえばx=1~6 (B-1)までで試せばよい。
# また、その数は増えていくのだから、
# NがB-1を超えた場合はB-1の値、NがB-1以下であればxの最大値で計算すればよい。

min = N
if N > B - 1:
    min = B - 1
print(A * min // B - A * (min // B))
