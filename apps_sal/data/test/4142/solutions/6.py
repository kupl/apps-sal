def resolve():
    s = input()
    step_odd = 'RUD'
    step_even = 'LUD'
    ans = 'Yes'
    for i, j in enumerate(s):
        if i % 2 == 0 and j not in step_odd:
            ans = 'No'
        elif i % 2 != 0 and j not in step_even:
            ans = 'No'
        else:
            pass
    print(ans)


resolve()
