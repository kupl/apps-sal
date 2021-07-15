'''
N人を円周上に配置し、M本の線分で結ぶ。
このとき、線分を回転させていっても同じ人のペアが生まれないようにする。

基本的には、上から順に結べばよい。
'''

from collections import deque

def main():
    N, M = list(map(int, input().split()))
    if N&1:
        '''
        ・Nが奇数の場合
        
        上から順に結ぶだけ。
        dequeに 1,2,3,...,M*2 を突っ込んで、両端から取り出してペアにする。
        '''
        q = deque(list(range(M*2)))
        while q:
            print((q.popleft()+1, q.pop()+1))
    else:
        '''
        [Nが偶数の場合]
        
        上から順に結ぶと、上下の線対称になり、同じ間隔のペアが生まれるためNG。
        → 半分以降は、1つずらしてペアを作っていく

        簡単に解決するため、
        ・上から順に奇数間隔ペアを作る
        ・下から順に偶数間隔ペアを作る
        この2つから、M個を順に、交互に取り出す。
        '''
        q1 = deque(list(range(N)))
        q2 = deque(list(range(N-1)))
        p1 = []
        while q1:
            p1.append((q1.popleft()+1, q1.pop()+1))
        p2 = []
        while len(q2)>=2:
            p2.append((q2.popleft()+1, q2.pop()+1))
        p2.reverse()
        for _ in range(M):
            print((*p1.pop()))
            p1, p2 = p2, p1


main()


