n = int(input())
kuro = input()
shiro = input()
katie = input()
kurod = {}
shirod = {}
katied = {}
kurov = 0
shirov = 0
katiev = 0
for c in kuro:
    if c not in kurod:
        kurod[c] = 1
    else:
        kurod[c] += 1
    kurov = max(kurov, kurod[c])
for c in shiro:
    if c not in shirod:
        shirod[c] = 1
    else:
        shirod[c] += 1
    shirov = max(shirov, shirod[c])
for c in katie:
    if c not in katied:
        katied[c] = 1
    else:
        katied[c] += 1
    katiev = max(katiev, katied[c])
kuroans = 0
shiroans = 0
katieans = 0
if len(kurod) > 1:
    kuroans = min(kurov + n, len(kuro))
elif n == 1 and len(kuro) > 1:
    kuroans = len(kuro) - 1
else:
    kuroans = len(kuro)
if len(shirod) > 1:
    shiroans = min(shirov + n, len(shiro))
elif n == 1 and len(shiro) > 1:
    shiroans = len(shiro) - 1
else:
    shiroans = len(shiro)
if len(katied) > 1:
    katieans = min(katiev + n, len(katie))
elif n == 1 and len(katie) > 1:
    katieans = len(katie) - 1
else:
    katieans = len(katie)
arr = [kuroans, shiroans, katieans]
arr = sorted(arr)
if arr[1] == arr[2]:
    print('Draw')
elif kuroans > max(shiroans, katieans):
    print('Kuro')
elif shiroans > max(kuroans, katieans):
    print('Shiro')
else:
    print('Katie')
