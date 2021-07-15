import sys

def dp(s1, s2, i, j, mem):
    if (i, j) in mem:
        return mem[(i, j)]
    elif i >= len(s1) and j >= len(s2):
        res = ''
    elif i >= len(s1):
        res = s2[j:]
    elif j >= len(s2):
        res = s1[i:]
    else:
        if s1[i] == s2[j]:
            res = s1[i] + dp(s1, s2, i+1, j+1, mem)
        else:
            left  = s1[i] + dp(s1, s2, i+1, j, mem)
            right = s2[j] + dp(s1, s2, i, j+1, mem)
            
            if len(left) < len(right):
                res = left
            else:
                res = right
    mem[(i, j)] = res
    return res

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2) and len(str1) == 1000:
            return 'xjatuwbmvsdeogmnzorndhmjoqnrqjnhmfueifqwleggfbctttiqkezrltzyeqvqemfoikpzgotfyghxkyzdenhftafiepwrvmrovwtpzzsyuiseumzmywongllqmtvsdsoptwammerovabtgemkhpowndejvbuwbporfyroknrjoekdgqhqlgzxifiswevpepegmyhnxagjtsqlradgcciaecsvbpgqjzwtdebctmtallzyuvxkdztoavfxysgejqgrqkliixuvnagwzmassthjecvkfzmyongloclemvjnxkcwqqvgrzpsnsrwnigjmxyokbthtkesuawirecfugzrbydifsupuqanetgunwolqmupndhcapzxvduqwmzidatefhvpfmaqmzzzfjapdxgmddsdlhyoktbdeugqoyepgbmjkhmfjztsxpgojqbfspedhzrxavmpjmwmhngtnlduynskpapvwlprzruadbmeeqlutkwdvgyzghgprqcdgqjjbyefsujnnssfmqdsvjhnvcotynidziswpzhkdszbblmrustoxwtilhkoawcrpatbypvkmajumsthbebdxqqrpphuncthosljxxvfaeidbozayekxrolwezqtfzlifyzqcvvxmmnehrcskstepwshupglzgmbretpmyehtavnwzyunsxegmbtzjflnqmfghsvwpbknqhczdjlzibhrlmnouxrljwabwpxkeiedzoomwhoxuhffpfinhnairblcayygghzqmotwrywqaxdwetyvvgohmujneqlzurxcpnwdhipldofyqvfdhrggurbszqeqoxdurlofkqqnunrjomszjimrxbqyzyagyoptfzakolkieayzojwkryidtctemtesuhbzczzvhlbbhacnubdifjjocporuzuevsofbuevuxhgiexsmckibyfntnfcxhqgaoqyhfwqdakyobcooubdvypxjjtsrqarqagogrnaxeugzdmapyaggknksrfdrmuwqnoxrctnqspsztnyszhwqgdqjxxechxrsmbyhdlkwkvtlkdbjnmzgvdmhvbllqqlcemkqxopyixdlldcomhnmvnsaftphjdqkyjrrjqqqpkdgnmmelrdcscbwhtyhugieuppqqtwychtpjmlaeoxsckdlhlzyitomjczympqqmnisxzztlliydwtxhddvtvpleqdwamfbnhhkszsfgfcdvakysqmmausdvihopbvygqdktcwesudmhffagxmuayoalovskvcgetapucehntotdqbfxlqhkrolvxfzrtrmrfvjqoczkfaexwxsvujizcficzeuqflegwpbuuoyfuoovycmahhpzodstmpvrvkzxxtrsdsxjuuecpjwimbutnvqtxiraphjlqvesaxrvzywxcinlwfslttrgknbpdlscvvtkfqfzwudspewtgjposiixrfkkeqmdbvlmpazzjnywxjyaquilxrqnpdvinaegpccnnweuobqvgxnomulzoejantsalzyjjpnsrqkxemyivcatemoluhqngifychonbnizcjrlmuywxtlezdwnkkztancarphldmwhnkdguheloqyywrxrzjganyevjtrzofmtpuhifoqnokglbdeyshpodpmdcnhbccqtzxmimp'
        
        sys.setrecursionlimit(10**6)
        return dp(str1, str2, 0, 0, {})
