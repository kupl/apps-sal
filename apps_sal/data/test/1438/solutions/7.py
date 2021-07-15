def main():
    def is_answer(ans):
        need = 0
        for i in range(n):
            need += max(0, a[i] * ans - b[i])
        return need <= k
    
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    left = 0
    right = 10 ** 18
    while (right - left > 1):
        middle = (left + right) // 2
        if (is_answer(middle)):
            left = middle
        else:
            right = middle
    print(left)
main()
