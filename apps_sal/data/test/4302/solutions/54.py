def count_coin_maximum():
    (a_button, b_button) = list(map(int, input().split()))
    if a_button == b_button:
        return a_button + a_button
    elif a_button > b_button:
        return a_button + max(a_button - 1, b_button)
    else:
        return b_button + max(b_button - 1, a_button)


print(count_coin_maximum())
