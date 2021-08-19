def abc064b(n: int, a_list: int) -> int:
    return max(a_list) - min(a_list)


n = int(input())
a_list = list(map(int, input().split()))
print(abc064b(n, a_list))
