
A, B, C, D = list(map(int, input().split()))

m = C // B  # 青木君の耐えうるターン
if C % B != 0:
    m = m + 1

n = A // D  # 高橋君の耐えうるターン
if A % D != 0:
    n = n + 1

if n >= m:
    print('Yes')
else:
    print('No')
