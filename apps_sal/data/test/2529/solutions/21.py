wd, bal = map(float, input().split())
if(wd % 5 == 0 and wd + 0.50 <= bal):
    bal = bal - wd - 0.5
    print(f'{bal:.2f}')
else:
    print(f'{bal:.2f}')
