class Solution:

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ans = 'Neither'
        if '.' in IP:
            seg = IP.split('.')
            if len(seg) == 4:
                if all((s.isdigit() and 0 <= int(s) < 256 and (not (s[0] == '0' and len(s) > 1)) for s in seg)):
                    ans = 'IPv4'
        elif ':' in IP:
            seg = IP.split(':')
            if len(seg) == 8:
                if all((0 < len(s) <= 4 and all((c in string.hexdigits for c in s)) for s in seg)):
                    ans = 'IPv6'
        return ans
