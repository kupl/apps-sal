def ans168(N: str):
    hon_list = ['2', '4', '5', '7', '9']
    pon_list = ['0', '1', '6', '8']
    bon_list = ['3']
    if N[-1] in hon_list:
        return 'hon'
    if N[-1] in pon_list:
        return 'pon'
    if N[-1] in bon_list:
        return 'bon'


N = input()
print(ans168(N))
