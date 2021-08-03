N = int(input())
A = [int(input()) for _ in range(5)]

# 一番輸送量が小さい経路で詰まる
# 一番輸送量が小さい経路を一番最初に通過すると考える
ans = -(-N // min(A)) + 4
print(ans)
