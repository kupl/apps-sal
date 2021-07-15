# coding: utf-8
import itertools
def main():
    n, m, q = map(int, input().split())
    matrix = []
    for _ in range(q):
        row = list(map(int, input().split()))
        matrix.append(row)
    # print(matrix)
    A = list(range(1, m+1))
    ans = 0
    for tmp_A in itertools.combinations_with_replacement(A, n):
        tmp_A = sorted(list(tmp_A))
        tmp_ans = 0
        for row in matrix:
            # print("row", row)
            # print("tmp_A", tmp_A)
            tmp = tmp_A[row[1] - 1] - tmp_A[row[0]- 1]
            if row[2] == tmp:
                tmp_ans += row[3]
        if tmp_ans >= ans:
            ans = tmp_ans
            
    print(ans)
    
main()
