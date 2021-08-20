for t in range(int(input())):
    n = int(input())
    st = input()
    ans = n
    if '1' in st:
        ans = max(ans, (n - st.find('1')) * 2, (st.rfind('1') + 1) * 2)
        ans = max(ans, n + st.count('1'))
    print(ans)
