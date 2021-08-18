n = int(input())
x = input()
s = ''.join(['0', x, '1'])
s1 = ''.join(['1', x, '0'])


def get_max(s):
    net_count = 0
    current_max = 0
    mp = {}
    for (i, item) in enumerate(s):
        if item == '0':
            net_count -= 1
        elif item == '1':
            net_count += 1
        if (mp.get(net_count, None) == None):
            mp[net_count] = i
        else:
            dist = i - mp[net_count]
            if dist > current_max:
                current_max = dist
    return current_max


print(min(get_max(s), get_max(s1)))
