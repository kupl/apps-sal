def solution(s):
    st = []
    ans = 0
    for i, j in enumerate(s):
        if j in open:
            st.append((i, j))
        if j in close:
            if not st:
                return ("Impossible")
            q, w = st.pop()
            if close.index(j) != open.index(w):
                ans += 1
    if st:
        return ("Impossible")
    return ans


s = str(input())
open = ['(', '{', '<', '[']
close = [')', '}', '>', ']']
print(solution(s))
