def main():
    s = input()
    t = input()
    s_list = []
    t_list = []
    for i in range(len(s)):
        s_list.append(s[i])
    for i in range(len(t)):
        t_list.append(t[i])
    s_list.sort()
    t_list.sort(reverse = True)
    #print(s_list,t_list)
    #if 'a'<'b':
        #print ('Yes')
    s_l = len(s_list)
    t_l = len(t_list)
    if s_l >= t_l:
        ans = 'No'
    else:
        ans = 'Yes'

    for i in range(min(s_l,t_l)):
        if s_list[i] == t_list[i]:
            continue
        elif s_list[i] > t_list[i]:
            return ('No')
        else:
            return('Yes')

    return ans

print((main()))

