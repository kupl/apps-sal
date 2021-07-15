#    ~####~~~#####~~~~####~~~######~~#####~~~#####~~~##~~##
#    ##~~##~~##~~##~~##~~##~~~~~##~~~##~~##~~##~~~~~~##~##
#    ##~~##~~#####~~~######~~~~##~~~~#####~~~####~~~~####
#    ##~~##~~##~~##~~##~~##~~~##~~~~~##~~##~~##~~~~~~##~##
#    ~####~~~##~~##~~##~~##~~######~~#####~~~#####~~~##~~##


class Read:
    @staticmethod
    def int():
        return int(input())

    @staticmethod
    def list(sep=' '):
        return input().split(sep)

    @staticmethod
    def list_int(sep=' '):
        return list(map(int, input().split(sep)))


def solve():
    n, m = Read.list_int()

    ans = []
    for i in range(n):
        ans.append(input())

    b = Read.list_int()
    result = 0
    for i in range(m):
        f = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0
        }
        for j in range(n):
            f[ans[j][i]] += 1

        max_f = 0
        for k in list(f.values()):
            if k > max_f:
                max_f = k
        result += max_f * b[i]
    print(result)


query_count = 1
# query_count = Read.int()
for j in range(query_count):
    solve()

