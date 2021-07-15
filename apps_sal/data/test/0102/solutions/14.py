
s2t20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
s2t10s = ['-', '-', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def text(score):
    if score <= 20:
        return s2t20[score]
    else:
        d10s, d1s = divmod(score, 10)
        if score % 10:
            return s2t10s[d10s] + '-' + s2t20[d1s]
        else:
            return s2t10s[d10s]

score = int(input())
print(text(score))
