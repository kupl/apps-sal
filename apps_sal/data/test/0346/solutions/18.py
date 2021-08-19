(n, m) = list(map(int, input().split(' ')))
tmp = list(map(int, input().split(' ')))
m_nums = list([int(x) - 1 for x in input().split(' ')])
m_list = [tmp[el] for el in m_nums]
_sum = sum(tmp) - sum(m_list)
m_list.sort()
while m_list and m_list[len(m_list) - 1] > _sum:
    _sum += m_list.pop()
print(_sum * 2 ** len(m_list))
