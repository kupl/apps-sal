N, M, C = map(int, input().split())
BM = list(map(int, input().split()))
ANM = [list(map(int, input().split())) for _ in range(N)]


class Answer:
    def __init__(self, N, M, C, BM, ANM):
        self.N = N
        self.M = M
        self.C = C
        self.BM = BM
        self.ANM = ANM

    def result(self):
        ans = 0
        for i in range(N):
            cnt = C
            for j in range(M):
                cnt += BM[j] * ANM[i][j]
            if cnt > 0:
                ans += 1
        print(ans)


info = Answer(N, M, C, BM, ANM)
info.result()
