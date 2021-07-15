import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    from scipy.sparse.csgraph import connected_components  # https://note.nkmk.me/python-scipy-connected-components/
    from scipy.sparse import csr_matrix
    
    N, M = map(int, input().split())  # 頂点数、辺数
    A, B, C = [0] * M, [0] * M, [1] * M  # A[i]からB[i]へコストC[i]の有向辺。
    # ただし、connected_components()では有向グラフも無向グラフとして扱われる
    for i in range(M):
        A[i], B[i] ,_= map(int, input().split())
        A[i] -= 1  # indexを調整
        B[i] -= 1
    
    csr = csr_matrix((C, (A, B)), shape=(N, N))
    # nは連結成分の個数。labelは各頂点が属する連結成分のラベル
    n, labels = connected_components(csr)
    print(n)

    
resolve()
